import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
