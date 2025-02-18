import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'DPOCycles': 1.0
        })
    )
