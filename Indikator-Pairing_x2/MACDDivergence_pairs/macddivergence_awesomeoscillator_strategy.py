import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_AwesomeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und AwesomeOscillator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'AwesomeOscillator': 1.0
        })
    )
