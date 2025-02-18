import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und BarStrength
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'BarStrength': 1.0
        })
    )
