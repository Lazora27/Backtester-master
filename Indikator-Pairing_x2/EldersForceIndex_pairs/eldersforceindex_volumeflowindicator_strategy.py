import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
