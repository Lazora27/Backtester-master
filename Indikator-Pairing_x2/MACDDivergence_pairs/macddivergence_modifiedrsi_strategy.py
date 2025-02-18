import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'ModifiedRSI': 1.0
        })
    )
