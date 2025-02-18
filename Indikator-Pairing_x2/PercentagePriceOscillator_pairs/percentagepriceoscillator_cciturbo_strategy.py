import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'CCITurbo': 1.0
        })
    )
