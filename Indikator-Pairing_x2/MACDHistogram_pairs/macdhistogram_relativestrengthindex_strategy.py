import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
