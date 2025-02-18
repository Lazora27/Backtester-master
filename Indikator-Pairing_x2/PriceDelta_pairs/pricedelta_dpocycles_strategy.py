import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und DPOCycles
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'DPOCycles': 1.0
        })
    )
