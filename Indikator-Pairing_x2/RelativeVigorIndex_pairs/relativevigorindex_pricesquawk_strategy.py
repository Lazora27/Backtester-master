import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'PriceSquawk': 1.0
        })
    )
