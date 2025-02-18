import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
