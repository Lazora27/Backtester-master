import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
