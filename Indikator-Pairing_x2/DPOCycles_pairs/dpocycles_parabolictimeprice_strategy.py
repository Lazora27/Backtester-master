import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
