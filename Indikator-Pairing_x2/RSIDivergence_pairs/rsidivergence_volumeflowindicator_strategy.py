import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
