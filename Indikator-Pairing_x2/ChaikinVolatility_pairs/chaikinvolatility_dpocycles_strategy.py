import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und DPOCycles
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'DPOCycles': 1.0
        })
    )
