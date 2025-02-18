import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
