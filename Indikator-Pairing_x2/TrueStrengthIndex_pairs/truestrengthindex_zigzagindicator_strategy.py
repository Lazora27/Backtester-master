import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
