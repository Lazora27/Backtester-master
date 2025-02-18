import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
