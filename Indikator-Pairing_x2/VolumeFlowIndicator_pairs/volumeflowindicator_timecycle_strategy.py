import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeFlowIndicator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeFlowIndicator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'VolumeFlowIndicator': 1.0,
            'TimeCycle': 1.0
        })
    )
