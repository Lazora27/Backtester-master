import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'SmoothedRSI': 1.0
        })
    )
