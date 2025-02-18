import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und BarStrength
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'BarStrength': 1.0
        })
    )
