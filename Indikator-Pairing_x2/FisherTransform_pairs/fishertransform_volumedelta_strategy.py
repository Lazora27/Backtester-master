import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'VolumeDelta': 1.0
        })
    )
