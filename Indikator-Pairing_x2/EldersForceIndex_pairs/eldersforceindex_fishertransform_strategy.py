import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und FisherTransform
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'FisherTransform': 1.0
        })
    )
