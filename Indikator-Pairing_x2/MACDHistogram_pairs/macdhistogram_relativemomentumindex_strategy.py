import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
