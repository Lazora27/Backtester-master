import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und CCITurbo
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'CCITurbo': 1.0
        })
    )
