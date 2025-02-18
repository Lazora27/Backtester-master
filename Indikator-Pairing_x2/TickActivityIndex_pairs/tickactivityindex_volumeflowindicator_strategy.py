import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
