import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
