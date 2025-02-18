import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und DPOCycles
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'DPOCycles': 1.0
        })
    )
