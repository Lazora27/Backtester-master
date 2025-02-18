import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
