import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_CVIRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und CVIRatio
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'CVIRatio': 1.0
        })
    )
