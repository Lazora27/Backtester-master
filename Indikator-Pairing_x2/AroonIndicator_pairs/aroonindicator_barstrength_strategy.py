import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und BarStrength
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'BarStrength': 1.0
        })
    )
