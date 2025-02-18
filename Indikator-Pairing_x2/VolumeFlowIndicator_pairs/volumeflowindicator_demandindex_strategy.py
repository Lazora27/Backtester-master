import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeFlowIndicator_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeFlowIndicator und DemandIndex
    """
    
    params = (
        ('indicators', {
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'VolumeFlowIndicator': 1.0,
            'DemandIndex': 1.0
        })
    )
