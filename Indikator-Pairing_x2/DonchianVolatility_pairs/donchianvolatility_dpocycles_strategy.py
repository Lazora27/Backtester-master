import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und DPOCycles
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'DPOCycles': 1.0
        })
    )
