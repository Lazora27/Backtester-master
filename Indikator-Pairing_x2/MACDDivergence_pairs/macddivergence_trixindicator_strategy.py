import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'TRIXIndicator': 1.0
        })
    )
