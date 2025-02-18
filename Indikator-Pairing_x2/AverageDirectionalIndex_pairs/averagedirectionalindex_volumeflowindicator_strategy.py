import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
