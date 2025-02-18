import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'FisherSignals': 1.0
        })
    )
