import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'ModifiedATR': 1.0
        })
    )
