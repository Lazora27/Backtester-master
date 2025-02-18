import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und DPOCycles
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'DPOCycles': 1.0
        })
    )
