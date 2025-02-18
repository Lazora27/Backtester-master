import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und FisherTransform
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'FisherTransform': 1.0
        })
    )
