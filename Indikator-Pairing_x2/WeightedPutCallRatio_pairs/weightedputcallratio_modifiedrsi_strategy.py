import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'ModifiedRSI': 1.0
        })
    )
