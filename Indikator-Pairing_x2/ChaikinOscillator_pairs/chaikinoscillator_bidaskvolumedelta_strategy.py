import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
