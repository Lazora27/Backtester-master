import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
