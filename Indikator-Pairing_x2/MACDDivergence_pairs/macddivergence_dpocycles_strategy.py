import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und DPOCycles
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'DPOCycles': 1.0
        })
    )
