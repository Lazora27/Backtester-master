import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'SmoothedRSI': 1.0
        })
    )
