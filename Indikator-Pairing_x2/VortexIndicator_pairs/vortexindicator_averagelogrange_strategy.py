import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'AverageLogRange': 1.0
        })
    )
