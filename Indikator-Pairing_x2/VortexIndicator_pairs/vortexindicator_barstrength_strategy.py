import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und BarStrength
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'BarStrength': 1.0
        })
    )
