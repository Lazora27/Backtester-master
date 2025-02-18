import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und BarStrength
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'BarStrength': 1.0
        })
    )
