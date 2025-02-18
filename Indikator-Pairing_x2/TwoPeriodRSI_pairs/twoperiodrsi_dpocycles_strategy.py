import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und DPOCycles
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'DPOCycles': 1.0
        })
    )
