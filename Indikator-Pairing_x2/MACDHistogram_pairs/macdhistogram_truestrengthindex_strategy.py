import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
