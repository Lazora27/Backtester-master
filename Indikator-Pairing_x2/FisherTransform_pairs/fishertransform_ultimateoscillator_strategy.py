import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'UltimateOscillator': 1.0
        })
    )
