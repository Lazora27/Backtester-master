import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
