import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und DemandIndex
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'DemandIndex': 1.0
        })
    )
