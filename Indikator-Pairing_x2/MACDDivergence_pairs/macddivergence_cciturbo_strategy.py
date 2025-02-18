import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und CCITurbo
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'CCITurbo': 1.0
        })
    )
