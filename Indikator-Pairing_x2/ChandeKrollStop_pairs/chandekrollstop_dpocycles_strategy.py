import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und DPOCycles
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'DPOCycles': 1.0
        })
    )
