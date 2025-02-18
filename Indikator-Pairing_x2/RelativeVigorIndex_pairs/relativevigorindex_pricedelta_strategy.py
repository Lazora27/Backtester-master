import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und PriceDelta
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'PriceDelta': 1.0
        })
    )
